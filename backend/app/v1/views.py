import io
import base64
import matplotlib.pyplot as plt

from rq.job import Job
from flask import Blueprint, jsonify, current_app


from lib import GeoPoint, GeoProfile


v01 = Blueprint('v1', __name__)

COEFF = 1000000


@v01.route('nextpoint_check/<string:job_id>')
def nextpoint_check(job_id):
    try:
        job = Job.fetch(job_id, connection=current_app.redis)
        job_status = job.get_status()
        job_result = job.result
        return jsonify(job_status=job_status,
                       latitude_b="{:.6f}".format(job_result['latitude_b']),
                       longitude_b="{:.6f}".format(job_result['longitude_b']),
                       p_a_elevation=job_result['p_a_elevation'],
                       p_b_elevation=job_result['p_b_elevation'],
                       )
    except Exception:
        job_status = None
        return jsonify(job_status=job_status)


@v01.route('nextpoint_add_task/<int(signed=True):la_a>/<int(signed=True):lon_a>/<int(signed=True):distance>/<int(signed=True):bearing>')
def nextpoint_add_task(la_a, lon_a, distance, bearing):
    rq_job = current_app.task_queue.enqueue('app.v1.tasks.nextpoint', la_a, lon_a, distance, bearing)
    return jsonify(job_id=rq_job.id,
                   job_status=rq_job.get_status(),
                   job_result=rq_job.result)


@v01.route('distance_check/<string:job_id>')
def distance_check(job_id):
    try:
        job = Job.fetch(job_id, connection=current_app.redis)
        job_status = job.get_status()
        job_result = job.result
        return jsonify(job_status=job_status,
                       distance="{:.3f}".format(job_result['distance']),
                       arc_distance="{:.3f}".format(job_result['arc_distance']),
                       az_a_b="{:.2f}".format(job_result['az_a_b']),
                       az_b_a="{:.2f}".format(job_result['az_b_a']),
                       p_a_elevation=job_result['p_a_elevation'],
                       p_b_elevation=job_result['p_b_elevation'],
                       )
    except Exception:
        job_status = None
        return jsonify(job_status=job_status)


@v01.route('distance_add_task/<int(signed=True):la_a>/<int(signed=True):lo_a>/<int(signed=True):la_b>/<int(signed=True):lo_b>')
def distance_add_task(la_a, lo_a, la_b, lo_b):
    rq_job = current_app.task_queue.enqueue('app.v1.tasks.distance', la_a, lo_a, la_b, lo_b)
    return jsonify(job_id=rq_job.id,
                   job_status=rq_job.get_status(),
                   job_result=rq_job.result)


@v01.route('profile/<int(signed=True):la_a>/<int(signed=True):lo_a>/<int(signed=True):la_b>/<int(signed=True):lo_b>')
def profile(la_a, lo_a, la_b, lo_b):
    (la_a, lo_a, la_b, lo_b) = (la_a / COEFF, lo_a / COEFF, la_b / COEFF, lo_b / COEFF)
    p_a = GeoPoint(la_a, lo_a)
    p_b = GeoPoint(la_b, lo_b)

    distance = p_a.distance_to(p_b) / 1000
    az_a_b = p_a.azimuth(p_b)
    az_b_a = p_b.azimuth(p_a)

    profile = GeoProfile(p_a, p_b)
    profile_chart = profile.get_chart_data()
    plt.rcParams["figure.figsize"] = (14, 9)
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.grid(True)
    ax.plot(profile_chart['distance'], profile_chart['relief'], label="Elevation", linestyle='solid', linewidth=0.5)
    ax.fill_between(profile_chart['distance'], profile_chart['relief'], min(profile_chart['relief']), color='darkgreen', alpha=.4)

    ax.set_xlabel('Distance (m)')
    ax.set_ylabel('Elevation (m)')

    plt.legend()
    plt.title(
        f'Profile from "{profile.startpoint.name}" {profile.startpoint.latitude} {profile.startpoint.longitude} '
        f'to "{profile.stoppoint.name}" {profile.stoppoint.latitude} {profile.stoppoint.longitude}\n'
        f'Distance {profile.length / 1000:.2f} km')
    f = io.BytesIO()
    plt.savefig(f, dpi=300, format='png')
    plt.close()
    graph = 'data:image/png;base64,' + base64.b64encode(f.getvalue()).decode('utf-8').replace('\n', '')
    return jsonify(distance="{:.3f}".format(distance),
                   az_a_b="{:.2f}".format(az_a_b),
                   az_b_a="{:.2f}".format(az_b_a),
                   p_a_elevation=p_a.elevation,
                   p_b_elevation=p_b.elevation,
                   graph=graph,
                   )

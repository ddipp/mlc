import io
import base64
import matplotlib.pyplot as plt

from rq.job import Job
from flask import Blueprint, jsonify, current_app


from lib import GeoPoint, GeoProfile


v01 = Blueprint('v1', __name__)

COEFF = 1000000


@v01.route('xy_check/<string:job_id>')
def xy_check(job_id):
    try:
        job = Job.fetch(job_id, connection=current_app.redis)
        job_status = job.get_status()
        job_result = job.result
    except Exception:
        job_status = None
        job_result = None
    return jsonify(job_status=job_status,
                   job_result=job_result)


@v01.route('xy/<int(signed=True):x>/<int(signed=True):y>')
def xy(x, y):
    rq_job = current_app.task_queue.enqueue('app.v1.tasks.addxy', x, y)
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


@v01.route('nextpoint/<int(signed=True):latitude_a>/<int(signed=True):longitude_a>/<int(signed=True):distance>/<int(signed=True):bearing>')
def nextpoint(latitude_a, longitude_a, distance, bearing):
    (latitude_a, longitude_a, distance, bearing) = (latitude_a / COEFF, longitude_a / COEFF, distance / COEFF * 1000, bearing / COEFF)
    p_a = GeoPoint(latitude_a, longitude_a)
    p_b = p_a.nextpoint(bearing, distance)
    return jsonify(latitude_b="{:.6f}".format(p_b.latitude),
                   longitude_b="{:.6f}".format(p_b.longitude),
                   p_a_elevation=p_a.elevation,
                   p_b_elevation=p_b.elevation,
                   )


@v01.route('distance/<int(signed=True):la_a>/<int(signed=True):lo_a>/<int(signed=True):la_b>/<int(signed=True):lo_b>')
def distance(la_a, lo_a, la_b, lo_b):
    (la_a, lo_a, la_b, lo_b) = (la_a / COEFF, lo_a / COEFF, la_b / COEFF, lo_b / COEFF)
    p_a = GeoPoint(la_a, lo_a)
    p_b = GeoPoint(la_b, lo_b)
    distance = p_a.distance_to(p_b) / 1000
    arc_distance = p_a.arc_distance_to(p_b) / 1000
    az_a_b = p_a.azimuth(p_b)
    az_b_a = p_b.azimuth(p_a)
    return jsonify(distance="{:.3f}".format(distance),
                   arc_distance="{:.3f}".format(arc_distance),
                   az_a_b="{:.2f}".format(az_a_b),
                   az_b_a="{:.2f}".format(az_b_a),
                   p_a_elevation=p_a.elevation,
                   p_b_elevation=p_b.elevation,
                   )

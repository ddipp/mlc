from rq.job import Job

from flask import current_app, Blueprint, render_template, url_for, jsonify

from .forms import DistanceForm, NextPointForm


v01 = Blueprint('v01', __name__)


@v01.route('/', methods=['GET'])
def index():
    return render_template('index.html', title="Home")


@v01.route('distance', methods=['GET'])
def distance():
    answer = {}
    distance_form = DistanceForm(url=url_for("v01.distance_calc"))
    return render_template('distance.html', title="Distance",
                           distance_form=distance_form, answer=answer)


@v01.route('distance_calc', methods=['POST'])
def distance_calc():
    distance_form = DistanceForm()
    if distance_form.validate_on_submit():
        rq_job = current_app.task_queue.enqueue('app.v01.tasks.distance',
                                                distance_form.latitude_a.data, distance_form.longitude_a.data,
                                                distance_form.latitude_b.data, distance_form.longitude_b.data)
    return jsonify(job_url=url_for("v01.distance_check", job_id=rq_job.id),
                   job_status=rq_job.get_status(),
                   job_result=rq_job.result)


@v01.route('distance_check/<string:job_id>', methods=['GET'])
def distance_check(job_id):
    try:
        job = Job.fetch(job_id, connection=current_app.redis)
        job_status = job.get_status()
        job_result = job.result
        return jsonify(job_status=job_status,
                       result={"distance": "{:.3f}".format(job_result['distance']),
                               "arc_distance": "{:.3f}".format(job_result['arc_distance']),
                               "az_a_b": "{:.3f}".format(job_result['az_a_b']),
                               "az_b_a": "{:.3f}".format(job_result['az_b_a']),
                               "a_elevation": job_result['a_elevation'],
                               "b_elevation": job_result['b_elevation'],
                               }
                       )
    except Exception:
        job_status = None
        return jsonify(job_status=job_status)


@v01.route('nextpoint', methods=['GET'])
def nextpoint():
    answer = {}
    nextpoint_form = NextPointForm(url=url_for("v01.nextpoint_calc"))
    return render_template('nextpoint.html', title="Next point",
                           nextpoint_form=nextpoint_form, answer=answer)


@v01.route('nextpoint_calc', methods=['POST'])
def nextpoint_calc():
    nextpoint_form = NextPointForm()
    if nextpoint_form.validate_on_submit():
        rq_job = current_app.task_queue.enqueue('app.v01.tasks.nextpoint', nextpoint_form.latitude.data, nextpoint_form.longitude.data,
                                                nextpoint_form.distance.data * 1000, nextpoint_form.bearing.data)
    return jsonify(job_url=url_for("v01.nextpoint_check", job_id=rq_job.id),
                   job_status=rq_job.get_status(),
                   job_result=rq_job.result)


@v01.route('nextpoint_check/<string:job_id>', methods=['GET'])
def nextpoint_check(job_id):
    try:
        job = Job.fetch(job_id, connection=current_app.redis)
        job_status = job.get_status()
        job_result = job.result
        return jsonify(job_status=job_status,
                       result={"b_latitude": "{:.7f}".format(job_result['b_latitude']),
                               "b_longitude": "{:.7f}".format(job_result['b_longitude']),
                               "a_elevation": job_result['a_elevation'],
                               "b_elevation": job_result['b_elevation'],
                               }
                       )
    except Exception:
        job_status = None
        return jsonify(job_status=job_status)

from rq.job import Job
from flask import Blueprint, jsonify, current_app, send_file


v01 = Blueprint('v1', __name__)

COEFF = 1000000


@v01.route('profile_check/<string:job_id>')
def profile_check(job_id):
    try:
        job = Job.fetch(job_id, connection=current_app.redis)
        job_status = job.get_status()
        job_result = job.result
        return jsonify(job_status=job_status,
                       distance="{:.3f}".format(job_result['distance']),
                       az_a_b="{:.2f}".format(job_result['az_a_b']),
                       az_b_a="{:.2f}".format(job_result['az_b_a']),
                       p_a_elevation=job_result['p_a_elevation'],
                       p_b_elevation=job_result['p_b_elevation'],
                       profile_name=job_result['filename'],
                       )
    except Exception:
        job_status = None
        return jsonify(job_status=job_status)


@v01.route('/profile_get/<string:filename>')
def profile_get(filename):
    return send_file(current_app.config['CACHE_DIR_PROFILE'] / filename, mimetype='image/png')


@v01.route('profile_add_task/<float:la_a>/<float:lo_a>/<float:la_b>/<float:lo_b>')
def profile_add_task(la_a: float, lo_a: float, la_b: float, lo_b: float):
    rq_job = current_app.task_queue.enqueue('app.v1.tasks.profile', la_a, lo_a, la_b, lo_b, current_app.config['CACHE_DIR_PROFILE'])
    return jsonify(job_id=rq_job.id,
                   job_status=rq_job.get_status(),
                   job_result=rq_job.result)


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


@v01.route('nextpoint_add_task/<float:la_a>/<float:lon_a>/<float:distance>/<float:bearing>')
def nextpoint_add_task(la_a: float, lon_a: float, distance: float, bearing: float):
    rq_job = current_app.task_queue.enqueue('app.v1.tasks.nextpoint', la_a, lon_a, distance * 1000, bearing)
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
                       az_a_b="{:.3f}".format(job_result['az_a_b']),
                       az_b_a="{:.3f}".format(job_result['az_b_a']),
                       p_a_elevation=job_result['p_a_elevation'],
                       p_b_elevation=job_result['p_b_elevation'],
                       )
    except Exception:
        job_status = None
        return jsonify(job_status=job_status)


@v01.route('distance_add_task/<float:la_a>/<float:lo_a>/<float:la_b>/<float:lo_b>')
def distance_add_task(la_a: float, lo_a: float, la_b: float, lo_b: float):
    rq_job = current_app.task_queue.enqueue('app.v1.tasks.distance', la_a, lo_a, la_b, lo_b)
    return jsonify(job_id=rq_job.id,
                   job_status=rq_job.get_status(),
                   job_result=rq_job.result)

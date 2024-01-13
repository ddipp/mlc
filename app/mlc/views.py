from rq.job import Job

from flask import current_app, Blueprint, render_template, url_for, jsonify, send_file
from flask_login import login_required, current_user

from .forms import DistanceForm, NextPointForm, ProfileForm
from .models import SiteModel

mlc = Blueprint('mlc', __name__, template_folder='templates')

############
# My sites #
############


@mlc.route('sites', methods=['GET'])
@login_required
def sites():
    sites = SiteModel.query.filter(SiteModel.user == current_user).order_by(SiteModel.dt.desc()).all()
    return render_template('mlc.sites.html', title="Sites",
                           sites=sites)

#################
# Server Status #
#################


@mlc.route('server_status', methods=['GET'])
def server_status():
    return jsonify(server_status="ok",
                   task_queue=len(current_app.task_queue))


###########
# Profile #
###########


@mlc.route('profile', methods=['GET'])
def profile():
    profile_form = ProfileForm(url=url_for("mlc.profile_calc"))
    return render_template('mlc.profile.html', title="Profile",
                           profile_form=profile_form)


@mlc.route('profile_calc', methods=['POST'])
def profile_calc():
    profile_form = ProfileForm()
    if profile_form.validate_on_submit():
        rq_job = current_app.task_queue.enqueue('app.mlc.tasks.radio_profile_graph',
                                                profile_form.tx_power.data, profile_form.frequency.data,
                                                profile_form.receiver_sensitivity.data,
                                                profile_form.antenna_gain_a.data, profile_form.latitude_a.data,
                                                profile_form.longitude_a.data, profile_form.height_a.data,
                                                profile_form.antenna_gain_b.data, profile_form.latitude_b.data,
                                                profile_form.longitude_b.data, profile_form.height_b.data,
                                                current_app.config['CACHE_DIR_PROFILE'])
    return jsonify(job_url=url_for("mlc.profile_check", job_id=rq_job.id),
                   job_status=rq_job.get_status(),
                   job_result=rq_job.result)


@mlc.route('profile_check/<string:job_id>', methods=['GET'])
def profile_check(job_id):
    try:
        job = Job.fetch(job_id, connection=current_app.redis)
        job_status = job.get_status()
        job_result = job.result
        return jsonify(job_status=job_status,
                       result={"distance": "{:.3f}".format(job_result['distance']),
                               "az_a_b": "{:.3f}".format(job_result['az_a_b']),
                               "az_b_a": "{:.3f}".format(job_result['az_b_a']),
                               "a_elevation": job_result['a_elevation'],
                               "b_elevation": job_result['b_elevation'],
                               'a_height': job_result['a_height'],
                               'b_height': job_result['b_height'],
                               'line_of_sight': job_result['line_of_sight'],
                               'visibility_in_0_6_fresnel_zone': job_result['visibility_in_0_6_fresnel_zone'],
                               'expected_signal_strength': job_result['expected_signal_strength'],
                               'filename': url_for("mlc.profile_get", filename=job_result['filename']),
                               }
                       )
    except Exception:
        job_status = None
        return jsonify(job_status=job_status)


@mlc.route('/profile_get/<string:filename>')
def profile_get(filename):
    return send_file(current_app.config['CACHE_DIR_PROFILE'] / filename, mimetype='image/png')


############
# Distance #
############


@mlc.route('distance', methods=['GET'])
def distance():
    distance_form = DistanceForm(url=url_for("mlc.distance_calc"))
    return render_template('mlc.distance.html', title="Distance",
                           distance_form=distance_form)


@mlc.route('distance_calc', methods=['POST'])
def distance_calc():
    distance_form = DistanceForm()
    if distance_form.validate_on_submit():
        rq_job = current_app.task_queue.enqueue('app.mlc.tasks.distance',
                                                distance_form.latitude_a.data, distance_form.longitude_a.data,
                                                distance_form.latitude_b.data, distance_form.longitude_b.data)
    return jsonify(job_url=url_for("mlc.distance_check", job_id=rq_job.id),
                   job_status=rq_job.get_status(),
                   job_result=rq_job.result)


@mlc.route('distance_check/<string:job_id>', methods=['GET'])
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


##############
# Next point #
##############


@mlc.route('nextpoint', methods=['GET'])
def nextpoint():
    answer = {}
    nextpoint_form = NextPointForm(url=url_for("mlc.nextpoint_calc"))
    return render_template('mlc.nextpoint.html', title="Next point",
                           nextpoint_form=nextpoint_form, answer=answer)


@mlc.route('nextpoint_calc', methods=['POST'])
def nextpoint_calc():
    nextpoint_form = NextPointForm()
    if nextpoint_form.validate_on_submit():
        rq_job = current_app.task_queue.enqueue('app.mlc.tasks.nextpoint',
                                                nextpoint_form.latitude.data, nextpoint_form.longitude.data,
                                                nextpoint_form.distance.data * 1000, nextpoint_form.bearing.data)
    return jsonify(job_url=url_for("mlc.nextpoint_check", job_id=rq_job.id),
                   job_status=rq_job.get_status(),
                   job_result=rq_job.result)


@mlc.route('nextpoint_check/<string:job_id>', methods=['GET'])
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
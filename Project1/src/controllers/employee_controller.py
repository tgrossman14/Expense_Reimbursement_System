import flask
from flask.helpers import url_for
from werkzeug.wrappers import request
from src.app import flask_app
from flask import make_response, redirect, session, request
import src.service.employee_service as es
import src.service.reimbursement_service as rs
from src.logging.logger import employee_log as log


@flask_app.route('/employee_dashboard/reimbursement', methods=['GET'])
def get_own_reimbursements():
    if "_employee_id" in session:
        employee_id = session['_employee_id']
        json = rs.get_all_reimbursements_by_employee_id(employee_id)
        if json:
            log.info(f'employee_id={employee_id}')
            return make_response(json, 200)
        else:
            log.error("Employee not found")
            return make_response("Employee not found", 404)
    else:
        return redirect(url_for("login"))


@flask_app.route('/employee_dashboard/reimbursement/new', methods=['POST'])
def post_new_reimbursement():
    if "_employee_id" in session:
        amount = request.form.get('reimbursement_amount')
        reason = request.form.get('reimbursement_reason')
        log.info(amount)
        log.info(reason)
        rs.post_new_reimbursement(amount, reason, session['_employee_id'])
        make_response("New reimbursement posted", 200)
        return redirect(url_for('employee_dashboard'))
    else:
        return redirect(url_for("login"))

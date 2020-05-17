from flask import Blueprint
main_blueprint = Blueprint('main', __name__)


@main_blueprint.before_request
def before_request():
	pass


@main_blueprint.after_request
def after_request(response):
	return response


from .views import (
	MemberDeposit,
	MemberOnlinePayment,
	MemberWithdrawal,
	PayCreate,
	PayManual,
	PayAutomatic,
	PayCancel,
	BankCallback,
	DFCreate,
	DFWithdraw,
)
main_blueprint.add_url_rule('/memberDeposit', view_func=MemberDeposit.as_view('memberDeposit'))
main_blueprint.add_url_rule('/memberOnlinePayment', view_func=MemberOnlinePayment.as_view('memberOnlinePayment'))
main_blueprint.add_url_rule('/memberWithdrawal', view_func=MemberWithdrawal.as_view('memberWithdrawal'))
main_blueprint.add_url_rule('/payCreate', view_func=PayCreate.as_view('payCreate'))
main_blueprint.add_url_rule('/payManual', view_func=PayManual.as_view('payManual'))
main_blueprint.add_url_rule('/payAutomatic', view_func=PayAutomatic.as_view('payAutomatic'))
main_blueprint.add_url_rule('/payCancel', view_func=PayCancel.as_view('payCancel'))
main_blueprint.add_url_rule('/bankCallback', view_func=BankCallback.as_view('bankCallback'))
main_blueprint.add_url_rule('/dfcreate', view_func=DFCreate.as_view('dfcreate'))
main_blueprint.add_url_rule('/dfwithdraw', view_func=DFWithdraw.as_view('dfwithdraw'))
from flask import request, abort
from flask.views import MethodView

from app.extensions import socketio


class MemberDeposit(MethodView):
	def get(self):
		data = {
			'OrderType': 100001,
			'OrderId': None
		}

		socketio.emit('foo response', {'data': data}, namespace='/foo', broadcast=True)
		return data

class MemberOnlinePayment(MethodView):
	def get(self):
		data = {
			'OrderType': 100002,
			'OrderId': None
		}

		socketio.emit('foo response', {'data': data}, namespace='/foo', broadcast=True)
		return data


class MemberWithdrawal(MethodView):
	def get(self):
		data = {
			'OrderType': 200001,
			'OrderId': None
		}

		socketio.emit('foo response', {'data': data}, namespace='/foo', broadcast=True)
		return data

'''订单创建'''
class PayCreate(MethodView):
	def get(self):
		data = {
			'Message': 300001,
		}

		socketio.emit('bar response', {'data': data}, namespace='/foo', broadcast=True)
		return data

'''订单手动匹配'''
class PayManual(MethodView):
	def get(self):
		data = {
			'Message': 400001,
		}

		socketio.emit('bar response', {'data': data}, namespace='/foo', broadcast=True)
		return data

'''订单自动匹配'''
class PayAutomatic(MethodView):
	def get(self):
		data = {
			'Message': 400002,
		}

		socketio.emit('bar response', {'data': data}, namespace='/foo', broadcast=True)
		return data

'''订单自动取消'''
class PayCancel(MethodView):
	def get(self):
		data = {
			'Message': 400003,
		}

		socketio.emit('bar response', {'data': data}, namespace='/foo', broadcast=True)
		return data

'''银行回调'''
class BankCallback(MethodView):
	def get(self):
		data = {
			'Message': 500001,
		}

		socketio.emit('bar response', {'data': data}, namespace='/foo', broadcast=True)
		return data

'''代付充值'''
class DFCreate(MethodView):
	def get(self):
		data = {
			'Message': 600001,
		}

		socketio.emit('bar response', {'data': data}, namespace='/foo', broadcast=True)
		return data

'''代付提现'''
class DFWithdraw(MethodView):
	def get(self):
		data = {
			'Message': 600002,
		}

		socketio.emit('bar response', {'data': data}, namespace='/foo', broadcast=True)
		return data
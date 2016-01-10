# -*- coding: utf-8 -*-


from openerp import tools
from openerp.osv import osv, fields


class res_partner(osv.osv):
	_inherit = 'res.partner'

	_columns = {
	    'auth_ids':fields.one2many('customer.auth.info','auth_id',"Authentication Info."),
	}

	


class customer_auth_info(osv.osv):
	_name = "customer.auth.info"
	_columns = {
	    'login' : fields.char('Login Id' ,required=True),
	    'password': fields.char('Password',required=True),
	    'customer_login_type':fields.many2one("customer.login.type",'Login Type'),
	    'auth_id':fields.many2one("res.partner",'Customer Name',readonly=True),
	    'private_key': fields.char('Private key'),
	    'public_key': fields.char('Public key'),
	    'website': fields.char('Website'),
	    'private_file': fields.binary('Private File'),
	    'public_file': fields.binary('Public File'),
	    'description':fields.text('Description'),
    }

class customer_login_type(osv.osv):
	_name = "customer.login.type"
	_columns = {
	    'name' : fields.char('Name' ,required=True),
	    }

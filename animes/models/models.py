# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta

class animes_animes(models.Model):
    _name = 'animes.animes'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Title")
    plot = fields.Char(string="Plot")
    genres = fields.Char(string="Genres")
    author = fields.Char(string="Author")
    studio = fields.Char(string="Studio")
    premiered = fields.Integer(string="Premiered")
    demographic = fields.Char(string="Demographic")
    episodes = fields.Integer(string="Episodes")
    poster = fields.Binary(string="Poster")
    thumb = fields.Binary(string="Thumb")
    actors = fields.One2many("animes.actors","anime",string="Actors")
    characters = fields.One2many("animes.characters","anime",string="Characters")
    users = fields.Many2many("animes.clientes","animes_users_rel","anime_id","user_id",string="Users")

    @api.model
    def create(self, values):
        res = super(animes_animes, self).create(values)

        self.env.cr.execute("""SELECT id FROM ir_model WHERE model = %s""", (str(self._name),))

        nuevo1 = self.env['mail.activity'].create({
            'user_id': 2,
            'res_model_id': self.env.cr.dictfetchall()[0]['id'],
            'res_id': res.id,
            'date_deadline': fields.Date.today(),
            'res_name': res.name,
            'note': "<p>TE CREÉ UNA TAREA .............</p>",
            'summary': "TareaNueva",
            'activity_type_id': 4,
            
        })


        return res

class animes_characters(models.Model):
    _name = 'animes.characters'

    name = fields.Char(string="Name")
    gender = fields.Char(string="Gender")
    age = fields.Char(string="Age")
    role = fields.Char(string="Role")
    thumb = fields.Char(string="Thumb")
    anime = fields.Many2one("animes.animes",string="Anime",required=True,ondelete="cascade")

class animes_actors(models.Model):
    _name = 'animes.actors'

    name = fields.Char(string="Name")
    gender = fields.Char(string="Gender")
    age = fields.Char(string="Age")
    character = fields.Char(string="Character")
    thumb = fields.Char(string="Thumb")
    anime = fields.Many2one("animes.animes",string="Anime",required=True,ondelete="cascade")

# class animes_users(models.Model):
#     _name = 'animes.users'

#     name = fields.Char(string="Name")
#     email = fields.Char(string="Email")
#     thumb = fields.Binary(string="Profile Picture")
#     animes = fields.Many2many("animes.animes","animes_users_rel","user_id","anime_id",string="Animes")

class animes_clientes(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    animes = fields.Many2many("animes.animes","animes_users_rel","user_id","anime_id",string="Animes")

class animes_users_rel(models.Model):
    _name = 'animes.users_rel'
    _table = 'animes_users_rel'
    _description = 'User anime relation'
    _rec_name = 'user_id'

    anime_id = fields.Many2one("animes.animes",string="Anime",ondelete="cascade",required=True)
    user_id = fields.Many2one("animes.clientes",string="Client",ondelete="cascade",required=True)

# class animes(models.Model):
#     _name = 'animes.animes'
#     _description = 'animes.animes'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

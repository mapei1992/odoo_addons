# -*- coding: utf-8 -*-

from odoo import models, fields, api


# 为产品类别增加编码规则字段
class product_category_sequences(models.Model):
    # _name = 'zzly_auto_sequences.zzly_auto_sequences'
    _description = '根据产品类别自动设置编码规则'
    _inherit = 'product.category'

    auto_sequences = fields.Many2one('ir.sequence', string='设置自动编码规则', help="""
    步骤：1、设置-一般设置-启用开发者模式；
2、设置-技术-序列 Sequences中定义编码规则，序列类型不能为空，并且不能重复；
3、未设置的会调取上级类别的编码规则；
4、只有首次创建的产品才会自动编码。""")

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100

# 实现自动编码
class product_category_sequences_auto_sequences(models.Model):
    _inherit = 'product.template'

# 循环获取上级类别的编码规则，直到找到
    def _get_category_sequence(self, category):
        """Recursively find the first non-empty auto_sequences in the category hierarchy."""
        if category.auto_sequences:
            return category.auto_sequences.code
        elif category.parent_id:
            return self._get_category_sequence(category.parent_id)
        return None
# 创建时自动编码，重写创建方法
    @api.model
    def create(self, vals):
        # Check if barcode is not provided and categ_id is set
        if not vals.get('barcode') and vals.get('categ_id'):
            categ_id = vals['categ_id']
            category = self.env['product.category'].browse(categ_id)
            sequence_code = self._get_category_sequence(category)

            if sequence_code:
                sequence = self.env['ir.sequence'].next_by_code(sequence_code)
                if sequence:
                    vals['barcode'] = sequence
                # 调用父类方法的返回
        return super(product_category_sequences_auto_sequences, self).create(vals)

# 增加自动编码规则配置字段
class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    contact_encoding_rule = fields.Many2one('ir.sequence', string='设置合作伙伴自动编码规则', help="""
    步骤：1、设置-一般设置-启用开发者模式；
2、设置-技术-序列 Sequences中定义编码规则,序列类型不能为空，并且不能重复；
3、只有首次创建联系人/合作伙伴/供应商时才会自动编码。""")

class partner_auto_sequence(models.Model):
    _inherit = 'res.partner'

    @api.model
    def create(self, vals):
        # 获取当前用户所在的公司
        current_user = self.env.user
        print(current_user)
        current_company = current_user.company_id.id
        print(current_company)
        current_company1 = self.env.context.get('allowed_company_ids', False)
        if  current_company1:
            current_company=current_company1[0]
        print(current_company)
        settings  = self.env['res.config.settings'].sudo().search([
            ('company_id', '=', current_company),
        ], limit=1)
        print(settings)
        if settings and not vals.get('ref') :
            contact_encoding_rule= settings.contact_encoding_rule.code
            sequence = self.env['ir.sequence'].next_by_code(contact_encoding_rule)
            if sequence:
                vals['ref'] = sequence
        return super(partner_auto_sequence, self).create(vals)
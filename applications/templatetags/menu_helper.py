#!coding:utf-8
from django.template import Library, Node, Variable
# from ..flatpage_tree.models import FlatPageTree
register = Library()


# class FpMenuNode(Node):
#     def __init__(self, max_level):
#         self.max_level = int(max_level) if max_level else None
#
#     def render(self, context):
#         tree = FlatPageTree.get_tree_help()
#         content = ''
#         previous_level = 0
#         for i in range(0, len(tree)):
#             current = tree[i]
#             cur_level = current.depth - 1
#             if self.max_level and cur_level >= self.max_level:
#                 continue
#
#             is_root = cur_level == 1
#
#             content += '</li></ul></div>' * (previous_level - cur_level)
#
#             if is_root:
#                 content += '<li class="item"><a href="{}">{}</a>'.format(
#                     current.flatpage.url, current.flatpage.title.encode('utf-8')
#                 )
#             else:
#                 if cur_level > previous_level:
#                     content += '<div class="subMenuBlock_{}"><ul class="menuItemList">'.format(cur_level)
#
#                 content += '<li class="item"><a class="link" href="{}"><span class="caption">{}</span></a>'.format(
#                     current.flatpage.url, current.flatpage.title.encode('utf-8'),
#                 )
#
#             previous_level = cur_level
#
#         content += '</li></ul></div>' * (previous_level - 2)
#         content += '</li>'
#
#         return content
#
#
# class FpMenuMetronicNode(Node):
#     def __init__(self, max_level):
#         self.max_level = int(max_level) if max_level else None
#
#     def render(self, context):
#         tree = FlatPageTree.get_tree_help_organizator()
#         content = ''
#         previous_level = 0
#         for i in range(0, len(tree)):
#             current = tree[i]
#             cur_level = current.depth
#             if self.max_level and cur_level >= self.max_level:
#                 continue
#
#             is_root = cur_level == 1
#
#             content += '</li></ul>' * (previous_level - cur_level)
#
#             if is_root:
#                 content += '<li class="kt-nav__item"><a class="kt-nav__link" href="{}"><span class="kt-nav__link-text">{}</span></a>'.format(
#                     current.flatpage.url, current.flatpage.title.encode('utf-8')
#                 )
#             else:
#                 if cur_level > previous_level:
#                     content += '<ul class="kt-nav__sub show" id="kt_nav_sub_{0}" role="tabpanel" aria-labelledby="m_nav_link_{0}" data-parent="#kt_nav" style="">'.format(cur_level)
#
#                 content += '<li class="kt-nav__item"><a class="kt-nav__link" href="{}"><span class="kt-nav__link-bullet kt-nav__link-bullet--line"><span></span></span><span class="kt-nav__link-text">{}</span></a>'.format(
#                     current.flatpage.url, current.flatpage.title.encode('utf-8'),
#                 )
#
#             previous_level = cur_level
#
#         content += '</li></ul>' * (previous_level - 2)
#         content += '</li>'
#
#         return content


# def render_flatpages_menu(parser, token):
#     keys = token.split_contents()
#     max_level = None
#     if len(keys) > 1:
#         _, max_level = keys
#
#     return FpMenuNode(max_level)
#
#
# def render_flatpages_menu_metronic(parser, token):
#     keys = token.split_contents()
#     max_level = None
#     if len(keys) > 1:
#         _, max_level = keys
#
#     return FpMenuMetronicNode(max_level)


# register.tag('render_flatpages_menu', render_flatpages_menu)
# register.tag('render_flatpages_menu_metronic', render_flatpages_menu_metronic)
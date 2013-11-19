from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def homepage():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    self['title'] = join_(u'Talk here! - Homepage')
    extend_([u'<h1>Talk here! </h1>\n'])

    return self

homepage = CompiledTemplate(homepage, 'templates/homepage.html')
join_ = homepage._join; escape_ = homepage._escape

# coding: utf-8
def layout (content):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<html>\n'])
    extend_([u'    <head>\n'])
    extend_([u'        <meta http-equiv="content-type" content="text/html; charset=utf-8" />\n'])
    extend_([u'        <title>', escape_(content.title, True), u'</title>\n'])
    extend_([u'        <link rel="stylesheet" href="static/css/bootstrap.min.css" title="" type="text/css" />\n'])
    extend_([u'        <link rel="stylesheet" href="static/css/bootstrap-theme.min.css" title="" type="text/css" />\n'])
    extend_([u'    </head>\n'])
    extend_([u'    <body>\n'])
    extend_([u'        ', escape_(content, False), u'\n'])
    extend_([u'        <script type="text/javascript" charset="utf-8" src="https://code.jquery.com/jquery-1.10.2.min.js"/>\n'])
    extend_([u'        <script type="text/javascript" charset="utf-8" src="static/js/bootstrap.min.js"/>\n'])
    extend_([u'    </body>\n'])
    extend_([u'</html>\n'])

    return self

layout = CompiledTemplate(layout, 'templates/layout.html')
join_ = layout._join; escape_ = layout._escape

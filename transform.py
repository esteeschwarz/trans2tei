import subprocess

SAXON_JAR = "SaxonHE12-5J/saxon-he-12.5.jar"


def base(xml_data, stylesheet):
    # java -jar saxon9he.jar -xsl:collect-blocks.xsl converted_body1.xml > converted_body.xml
    # output = subprocess.check_output(["java", "-jar", "saxon-he-10.5.jar", "-xsl:{}".format(stylesheet), infile])
    # return output.decode()

    command = ["java", "-jar", SAXON_JAR, "-xsl:{}".format(stylesheet), "-s:-"]
    p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = p.communicate(input=xml_data.encode())[0]
    return output.decode()


def page2tei(input_file):
    stylesheet = "page2tei/page2tei-0.xsl"
    command = ["java", "-jar", SAXON_JAR, "-xsl:{}".format(stylesheet), "-s:{}".format(input_file)]
    p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = p.communicate()[0]
    return output.decode()


def postprocess_page2tei(xml_data):
    stylesheet = "xslt/postprocess-page2tei.xsl"
    return base(xml_data, stylesheet)


def remove_position_data(xml_data):
    stylesheet = "xslt/remove-position-data.xsl"
    return base(xml_data, stylesheet)


def join_paragraphs(xml_data):
    stylesheet = "xslt/join-paragraphs.xsl"
    return base(xml_data, stylesheet)


def page_numbers(xml_data):
    stylesheet = "xslt/page-numbers.xsl"
    return base(xml_data, stylesheet)


def move_footnotes(xml_data):
    stylesheet = "xslt/move-footnotes.xsl"
    return base(xml_data, stylesheet)


def disconnect_style_and_type(xml_data):
    stylesheet = "xslt/disconnect-style-and-type.xsl"
    return base(xml_data, stylesheet)


def collect_blocks(xml_data):
    stylesheet = "xslt/collect-blocks.xsl"
    return base(xml_data, stylesheet)


def simplify_hi(xml_data):
    stylesheet = "xslt/simplify-hi.xsl"
    return base(xml_data, stylesheet)


def expand_hi(xml_data):
    stylesheet = "xslt/expand-hi.xsl"
    return base(xml_data, stylesheet)


def id_to_div(xml_data):
    stylesheet = "xslt/id-to-div.xsl"
    return base(xml_data, stylesheet)


def bibliography_elements(xml_data):
    stylesheet = "xslt/bibliography.xsl"
    return base(xml_data, stylesheet)


def woelfflin_elements(xml_data):
    stylesheet = "xslt/woelfflin-elements.xsl"
    return base(xml_data, stylesheet)

def indent(xml_data):
    stylesheet = "xslt/indent.xsl"
    return base(xml_data, stylesheet)

def remove_lb(xml_data):
    stylesheet = "xslt/remove-lb.xsl"
    return base(xml_data, stylesheet)

def remove_pb(xml_data):
    stylesheet = "xslt/remove-pb.xsl"
    return base(xml_data, stylesheet)

#
# Tabulatori per prezzi allineati a destra
# ⁅ ⁆
#
#
#
# <pb facs="#facs_121" n="121" xml:id="img_0121" />
#
# <fw type="page" place="bottom" facs="#facs_121_r_3_1">
#                     <lb facs="#facs_121_tl_41" n="N001" />105</fw>

<!-- <?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    exclude-result-prefixes="xs math"
    version="3.0">
    
</xsl:stylesheet> -->

<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" indent="yes"/>
    
    <!-- Template to match the root element -->
    <xsl:template match="/">
        <html>
            <head>
                <title><xsl:value-of select="topic/title"/></title>
                <style>
                    body { font-family: Arial, sans-serif; margin: 20px; }
                    h1 { color: navy; }
                    h2 { color: darkgreen; }
                    p, ul { font-size: 14px; }
                    ul { list-style-type: disc; margin-left: 20px; }
                    li { margin-bottom: 5px; }
                </style>
            </head>
            <body>
                <h1><xsl:value-of select="topic/title"/></h1>
                <xsl:apply-templates select="topic/body"/>
            </body>
        </html>
    </xsl:template>
    
    <!-- Template to match the body element -->
    <xsl:template match="body">
        <xsl:apply-templates/>
    </xsl:template>
    
    <!-- Template to match paragraph elements -->
    <xsl:template match="p">
        <p><xsl:value-of select="."/></p>
    </xsl:template>
    
    <!-- Template to match unordered list elements -->
    <xsl:template match="ul">
        <ul>
            <xsl:apply-templates select="li"/>
        </ul>
    </xsl:template>
    
    <!-- Template to match list item elements -->
    <xsl:template match="li">
        <li><xsl:value-of select="."/></li>
    </xsl:template>
</xsl:stylesheet>
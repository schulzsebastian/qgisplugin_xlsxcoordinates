# -*- coding: utf-8 -*-
"""
/***************************************************************************
 XlsxCoordinates
                                 A QGIS plugin
 Get coordinates from XLSX file
                             -------------------
        begin                : 2015-11-01
        copyright            : (C) 2015 by schulzsebastian
        email                : schulz.siwy@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load XlsxCoordinates class from file XlsxCoordinates.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .xlsx_coordinates import XlsxCoordinates
    return XlsxCoordinates(iface)

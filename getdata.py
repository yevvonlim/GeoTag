from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_exif(filename):
    exif = Image.open(filename)._getexif()
    gpsinfo = {}
    if exif != None:
        # iterating over all EXIF data fields
        for tag_id in exif:
        # get the tag name, instead of human unreadable tag id
            tag = TAGS.get(tag_id, tag_id)
            if tag == "GPSInfo":    
                for key in exif[tag_id].keys():
                    gpstag = GPSTAGS.get(key, key)
                    gpsinfo[gpstag] = exif.get(tag_id)[key]
                     
    return gpsinfo       


def get_coordinates(info):
    coordi = {}
    for key in ['Latitude', 'Longitude']:
        if ('GPS'+key in info) and ('GPS'+key+'Ref' in info):
            e = info['GPS'+key]
            ref = info['GPS'+key+'Ref']

            if (len(e) != 3) and (len(ref) != 3):
                coordi[key] = ( str(e[0][0]/e[0][1]) + '°' +
                                str(e[1][0]/e[1][1]) + '′' +
                                str(e[2][0]/e[2][1]) + '″ ' +
                                ref )
            else:
                coordi[key] = ( str(e[0]) + '°' +
                                str(e[1]) + '′' +
                                str(e[2]) + '″ ' +
                                ref )
        else:
            return False
    return [coordi['Latitude'], coordi['Longitude']]


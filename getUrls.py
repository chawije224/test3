import requests, xmltodict, json

def getUrl(mpdURL):
    r=requests.get(url=mpdURL)
    r.raise_for_status()
    xml=xmltodict.parse(r.text)
    mpd=json.loads(json.dumps(xml))
    periods=mpd['MPD']['Period']
    for ad_set in periods['AdaptationSet']:
        if ad_set['@contentType'] == 'video':
            for t in ad_set['Representation']:
                if t['@height'] == '360':
                    vid = t['BaseURL']
        else:
            aud = ad_set['Representation']['BaseURL']

    return vid, aud          

from rest_framework import serializers


def validator_scan_links(value):
    """ Check link """
    url_https = "https://"
    url_http = "http://"

    if url_https in value:
        if url_https + "youtube.com" not in value:
            raise serializers.ValidationError("You can not use this link.")

    if url_http in value:
        raise serializers.ValidationError("You can not use this link.")
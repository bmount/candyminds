function (doc) {
    if (doc.latest) {
        return {'code':302, 'headers':{'Location': "http://" + doc.latest}};
    } else {
    return {'body':'Check configuration'};
    }
}

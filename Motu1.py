import marshal,zlib,base64
exec(zlib.decompress(base64.b64decode("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")))

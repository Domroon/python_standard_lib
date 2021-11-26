import codecs

laughing_smiley = "\U0001F602" # replace '+' with 000
print(laughing_smiley) 

encoded_smiley = codecs.encode(laughing_smiley)
print("encoded: ")
print(encoded_smiley)

decoded_smiley = codecs.decode(encoded_smiley)
print("decoded: ")
print(decoded_smiley)

print("codec info for utf-8:")
codec_info_obj = codecs.lookup('utf-8')
print(f'name: {codec_info_obj.name}')
print(f'encode: {codec_info_obj.encode}')
print(f'decode: {codec_info_obj.decode}')
print(f'incrementalencoder: {codec_info_obj.incrementalencoder}')
print(f'incrementaldecoder: {codec_info_obj.incrementaldecoder}')
print(f'streamwriter: {codec_info_obj.streamwriter}')
print(f'streamreader: {codec_info_obj.streamreader}')
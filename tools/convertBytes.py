# 7/2/2022
# The is from pytutorial.com, this not my code.
def convert_bytes(nbytes):
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])


# Convert bytes to b, B, KB, MB, GB
# 1024 kilobytes (KB) = 1 Megabyte (MB)
# 1024 Megabyte (MB) = 1 Gigabyte (GB)
# When you are converting from a smaller unit to a larger one you divide
# create a function to that take three arguments ;
# unit to convert FROM (kb)
# unit to convert TO
# value of that unit 
# Check if the user wants to convert from a smaller to a larger unit. 
# if so then divide by 1024
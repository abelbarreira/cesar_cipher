# How to use it
# python caesar.py -k <key> -m <mode> -i <input_file> -o <output_file>
#
#   <key> as an integer
#   <mode> as Enc or Dec
#   <input_file>
#   <output_file>

import sys, getopt

def caesar(data, key, mode):
    alphabet = 'abcdefghijklmnñopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ'
    new_data = ''
    for c in data:
        # Shift character
        index = alphabet.find(c)
        if index == -1:
            # Character not found
            new_data += c
        else:
            # Shift it based on key and mode
            if mode == "Enc":
              new_index = index + key
            else:
              new_index = index - key
            new_index %= len(alphabet)
            new_data += alphabet[new_index:new_index+1]
    # Return the ciphered text
    return new_data

if __name__ == '__main__':
    syntax = 'k:m:i:o:'
    # Default arguments
    key = 1
    mode = "Enc"
    out_file = 'out.txt'
    in_file = 'in.txt'
    try:
        opts, args = getopt.getopt(sys.argv[1:], syntax)
        for o, a in opts:
            if o == '-k':
                key = int(a)
            elif o == '-m':
                mode = str(a)
            elif o == '-i':
                in_file = a
            elif o == '-o':
                out_file = a

        # Read file
        with open(in_file, 'rt') as f:
            data = f.read()
        # Translate it
        new_data = caesar(data, key, mode)
        with open(out_file, 'wt') as f:
            f.write(new_data)

    except getopt.GetoptError as err:
        print('Error parsing args:', err)
        sys.exit(1)
    except Exception as e:
        print('Error', e)
        sys.exit(2)

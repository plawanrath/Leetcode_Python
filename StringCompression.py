"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, 
be stored in the input character array chars. Note that group lengths that are 10 
or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
"""
def compress(chars):

    length = len(chars)

    # make it a bit faster
    if length < 2:
        return length

    # the start position of the contiguous group of characters we are currently reading.
    anchor = 0

    # position to Write Next
    # we start with 0 then increase it whenever we write to the array
    write = 0

    # we go through each caharcter till we fiand a pos where the next is not equal to it
    # then we check if it has appeared more than once using the anchor and r(read) pointers
    # 1. iterate till we find a diffrent char
    # 2. record the no. of times the current char was repeated
    for pos, char in enumerate(chars):

        # check if we have reached the end or a different char
        # check if we are end or the next char != the current
        if (pos + 1) == length or char != chars[pos+1]:
            chars[write] = char
            write += 1

            # check if char has been repeated
            # have been duplicated if the read pointer is ahead of the anchor pointer
            if pos > anchor:
                # check no. of times char has been repeated
                repeated_times = pos - anchor + 1

                # write the number
                for num in str(repeated_times):
                    chars[write] = num
                    write += 1

            # move the anchor to the next char in the iteration
            anchor = pos + 1

    return write
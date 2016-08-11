def isInterleave(s1,s2,s3):
    global count
    count=0
    if len(s1)+len(s2)!=len(s3):
        return False
    def check(s1,s2,s3):
        global count
        # print s1,s2,s3
        if not count:
            if not s1 or not s2 or not s3:
                if not s1 and s2 == s3:
                    count=1
                elif not s2 and s1 == s3:
                    count=1
                return
            if s1[0]==s2[0] and s2[0]==s3[0]:
                check(s1[1:],s2,s3[1:])
                check(s1,s2[1:],s3[1:])
            elif s1[0]==s3[0]:
                check(s1[1:],s2,s3[1:])
            elif s2[0]==s3[0]:
                check(s1,s2[1:],s3[1:])
    check(s1,s2,s3)
    # print count
    return count==1
s1="bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
s2="babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
s3="babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
s4='aadbbbaccc'

print isInterleave(s1,s2,s3)

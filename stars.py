import sys

def draw_stars(num):
    for count in range(0, len(num)):
        for count2 in range(0,num[count]):
            sys.stdout.write('*')
        print '\n'

def draw_stars2(num):
    for count in range (0, len(num)):
        c = '*'
        if isinstance(num[count], basestring):
            c = num[count][:1]
            for count2 in range (0,len(num[count])):
                sys.stdout.write('%s' % c)
        else:
            for count2 in range (0,num[count]):
                sys.stdout.write('%s'% c)
        print '\n'

x = ["aaaaa",2,3,"kjdfhjsdfkjhsdf",5]

draw_stars2(x)

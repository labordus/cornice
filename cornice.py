#!/usr/bin/env python
# cornice.py: entry point of Cornice
# arch-tag: entry point of Cornice
# author: Alberto Griggio <agriggio@users.sourceforge.net>
# license: GPL

import sys, os
import getopt

sys.path.insert(0, os.path.abspath(os.path.dirname(sys.argv[0])))

import remote


def main():
    slideshow = False
    path = None
    quickstart = False

    try:
        options, args = getopt.getopt(sys.argv[1:], 'shq',
                                      ['slideshow', 'help', 'quickstart'])
    except getopt.GetoptError:
        usage()
    for o, a in options:
        if o in ('-s', '--slideshow'):
            slideshow = True
        elif o in ('-q', '--quickstart'):
            quickstart = True
        elif o in ('-h', '--help'):
            usage(False)

    if args:
        path = os.path.abspath(os.path.expanduser(args[0]))

    if remote.ping():
        if slideshow:
            cmd = 'SLIDESHOW'
        else:
            cmd = 'RAISE'
        if path and not slideshow:
            import fileops
            if fileops.isfile(path): cmd = 'SHOW'
            else: cmd = 'BROWSE'
        status = remote.do_command(cmd, path or "")
        sys.exit(status)
    else:
        import fixdc
        import main
        main.main(path, slideshow, quickstart)


def usage(err=True):
    if err: stream = sys.stderr
    else: stream = sys.stdout
    print >> stream, """Usage: %s [OPTIONS] [PATH]
Valid OPTIONS:
-s, --slideshow:  starts a slideshow of the images in PATH (that must be given)
-q, --quickstart: quick start mode
-h, --help:       shows this message and exits

If there are no options and PATH is given, shows the image at PATH\
""" % os.path.basename(sys.argv[0])
    sys.exit(err)


if __name__ == '__main__':
    main()

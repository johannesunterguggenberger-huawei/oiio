#!/usr/bin/env python 

# Slightly bump allowable failures, for slightly shifting font rendering
# with changed freetype versions.
failpercent *= 2.0

# test subimages
command += oiiotool ("--pattern constant:color=0.5,0.0,0.0 64x64 3 " +
                     "--pattern constant:color=0.0,0.5,0.0 64x64 3 " +
                     "--siappend -d half -o subimages-2.exr")
command += oiiotool ("--pattern constant:color=0.5,0.0,0.0 64x64 3 --text A -attrib oiio:subimagename layerA " +
                     "--pattern constant:color=0.0,0.5,0.0 64x64 3 --text B -attrib oiio:subimagename layerB " +
                     "--pattern constant:color=0.0,0.0,0.5 64x64 3 --text C -attrib oiio:subimagename layerC " +
                     "--pattern constant:color=0.5,0.5,0.0 64x64 3 --text D -attrib oiio:subimagename layerD " +
                     "--siappendall -d half -o subimages-4.exr")
command += oiiotool ("subimages-4.exr --subimage 3 -o subimageD3.exr")
command += oiiotool ("subimages-4.exr --subimage layerB -o subimageB1.exr")
command += oiiotool ("subimages-2.exr --sisplit -o:all=1 subimage%d.exr")

# test that we can set attributes on individual subimages
command += oiiotool ("subimages-4.exr --attrib:subimages=0 Beatle John --attrib:subimages=1 Beatle Paul --attrib:subimages=2 Beatle George --attrib:subimages=3 Beatle Ringo -o gpgr.exr")
command += info_command ("-a -v gpgr.exr", safematch=1)

# Outputs to check against references
outputs = [ 
            "subimages-2.exr", "subimages-4.exr",
            "subimage1.exr", "subimage2.exr",
            "subimageD3.exr", "subimageB1.exr",
            "out.txt"
          ]

#print "Running this command:\n" + command + "\n"

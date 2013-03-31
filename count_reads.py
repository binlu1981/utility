#!/usr/bin/env python
from optparse import OptionParser
import pysam

################################################################################
# count_reads.py
#
# Count the reads in a BAM file, by relying on the multimap count tag.
################################################################################


################################################################################
# main
################################################################################
def main():
    usage = 'usage: %prog [options] <bam>'
    parser = OptionParser(usage)
    #parser.add_option('-d', dest='debug', default=False, action='store_true', help='Print debug output to read_counts.txt')
    (options,args) = parser.parse_args()

    if len(args) != 1:
        parser.error('Must provide BAM file')

    # initialize
    count = 0.0

    # process
    for aligned_read in pysam.Samfile(args[0]):
        if aligned_read.is_paired:
            count += 0.5/aligned_read.opt('NH')
        else:
            count += 1.0/aligned_read.opt('NH')

    # output
    print count


################################################################################
# __main__
################################################################################
if __name__ == '__main__':
    main()
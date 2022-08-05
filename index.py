with open('code/input/sAdaptive4.src') as infile:
    file_line_limit = 5000
    counter = -1
    file_index = 0
    outfile = None
    for line in infile.readlines():
        counter += 1
        if counter % file_line_limit == 0:
            # close old file
            if outfile is not None:
                outfile.close()
            # create new file
            file_index += 1
            outfile = open('code/output/sAdaptive4_%03d.src' % file_index, 'w')
        # write to file
        outfile.write(line)
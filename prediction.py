import argparse
import os
import utils


ap = argparse.ArgumentParser()
ap.add_argument('-i','--input-dir', type=str, default='pred', help="input directory (default = pred)", metavar='')
ap.add_argument('-p','--predictor', type=str, default='predictor.dat', help="trained shape prediction model (default = predictor.dat)", metavar='')
ap.add_argument('-o','--out-file', type=str, default='output.xml', help="output file name (default = output.xml)", metavar='')
ap.add_argument('-l','--ignore-list', nargs='*', type=int, default=None, help=" (optional) prevents landmarks of choice from being output", metavar='')






args = vars(ap.parse_args())

utils.predictions_to_xml(args['predictor'], dir=args['input_dir'],ignore=args['ignore_list'],out_file=args['out_file'])
utils.dlib_xml_to_tps(args['out_file'])

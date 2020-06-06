# pip install ConfigArgParse
# reference: https://github.com/bw2/ConfigArgParse
# reference: https://github.com/wbaek/theconf
import configargparse

# process .yaml file
file_parser = configargparse.DefaultConfigFileParser 

# singleton
parser = configargparse.get_argument_parser(config_file_parser_class=file_parser) 
parser.add('-c', '--config', required=True, is_config_file=True, help='config file path') 
# must add all argument in config file (like .yaml)
parser.add_argument('--model', type=str) 
parser.add_argument('--dataset', type=str) 
parser.add_argument('--batch', type=int)
parser.add_argument('--epoch', type=int)

def fn1():
    args = parser.parse_args()     
    print('model type: ', args.model)
    print('dataset: ', args.dataset)

def fn2():
    args = parser.parse_args()
    print('batch: ', args.batch)
    print('epoch: ', args.epoch)

if __name__ == '__main__':
    fn1()
    fn2()

import csv
import torch

class AverageMeter(object):
    """Computes and stores the average and current value"""

    def __init__(self):
        self.reset()

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count


class Logger(object):

    def __init__(self, path, header):
        self.log_file = open(path, 'w')
        self.logger = csv.writer(self.log_file, delimiter='\t')

        self.logger.writerow(header)
        self.header = header

    def __del(self):
        self.log_file.close()

    def log(self, values):
        write_values = []
        for col in self.header:
            assert col in values
            write_values.append(values[col])

        self.logger.writerow(write_values)
        self.log_file.flush()
        
def calculate_accuracy(outputs, targets):
    batch_size = targets.size(0)
    targets = targets.clone().to(dtype=torch.uint8)
    pred = outputs.gt(0.5)
    pred = pred.t()
    targets = targets.ge(1)
    correct = pred.eq(targets.view(1, -1))
    n_correct_elems = correct.float().sum().item()
    #print('batch_size:{} n_correct_elems:{}'.format(batch_size,n_correct_elems))
    return n_correct_elems / batch_size

import modules.gio_logger as utils
import os
import sys

class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def make_tree1 ():
    tree = Tree(2)
    log.debug('TREE: %s' % tree.data)
    tree.left = Tree(8)
    log.debug('TREE.LEFT: %s' % tree.left.data)
    tree.left.left = Tree(1)
    log.debug('TREE.LEFT.LEFT: %s' % tree.left.left.data)
    tree.left.right = Tree(3)
    log.debug('TREE.LEFT.RIGHT: %s' % tree.left.right.data)
    tree.right = Tree(9)
    log.debug('TREE.RIGHT: %s' %  tree.right.data)
    tree.right.left = Tree(4)
    log.debug('TREE.RIGHT.LEFT: %s' % tree.right.left.data)
    tree.right.right = Tree(5)
    log.debug('TREE.RIGHT.LEFT: %s' % tree.right.right.data)
    return tree

def make_tree2 ():
    tree = Tree(1)
    log.debug('TREE: %s' % tree.data)
    tree.left = Tree(8)
    log.debug('TREE.LEFT: %s' % tree.left.data)
    tree.left.right = Tree(3)
    log.debug('TREE.LEFT.RIGHT: %s' % tree.left.right.data)
    tree.right = Tree(4)
    log.debug('TREE.RIGHT: %s' % tree.right.data)
    tree.right.right = Tree(5)
    log.debug('TREE.RIGHT.RIGHT: %s' % tree.right.right.data)
    tree.right.right.right = Tree(7)
    log.debug('TREE.RIGHT.RIGHT.RIGHT: %s' % tree.right.right.right.data)
    return tree

def get_depth (tree):
    #log.debug("Executing get_depth function")
    if tree is None:
        return 0;

    else:
        left_depth  = get_depth(tree.left)
        log.debug('get_depth - LEFT_DEPTH: %s' % left_depth)
        right_depth = get_depth(tree.right)
        log.debug('get_depth - RIGHT_DEPTH: %s' % right_depth)

        if (left_depth > right_depth):
            log.debug('get_depth - DEPTH: %s' % (left_depth+1))
            return left_depth+1
        else:
            log.debug('get_depth - DEPTH: %s' % (right_depth+1))
            return right_depth+1


def return_tuple_value_level (tree, level=0, result=[]):
    #log.debug("Executing return_tuple_value_level function")
    if tree is None:
        return;

    else:
        log.debug("return_tuple_value_level tree.data = %s" % tree.data )
        log.debug("return_tuple_value_level level = %s" % level)
        left_depth  = return_tuple_value_level(tree.left,  level+1, result)
        right_depth = return_tuple_value_level(tree.right, level+1, result)
        level-1
        result.append([level, tree.data])
        log.debug("return_tuple_value_level append tuple = %s" % ([level, tree.data]))
        log.debug("return_tuple_value_level result tuple = %s" % result)
        return result

def sort_by_level(tree):
    result = []
    depth = get_depth(tree)
    tuples = return_tuple_value_level(tree, result=[])
    log.debug("sort_by_level - Entering nested loops in sort_by_level function")
    for d in range(depth):
        for r in range(len(tuples)):
            if tuples[r][0] == d:
                result.append(tuples[r][1])
                log.debug("sort_by_level - Append to sorted list tuples[%d][1] value = %d" % (r,tuples[r][1]))
    return result



def main ():

    if os.environ.get('GIO_LOG_LEVEL') is None:
        log.warning("Set OS Variable GIO_LOG_LEVEL to 'debug' for more information.")

    log.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 1 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    log.info("Create tree1")
    tree1 = make_tree1()

    log.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    log.info("Creating tree2")
    tree2 = make_tree2()

    log.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 3 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    log.info("Max depth of Tree1 is %d" % get_depth(tree1))

    log.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 4 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    log.info("Max depth of Tree2 is %d <<<<<<" % get_depth(tree2))

    log.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 5 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    log.info("List of Tuple Value,Level for Tree1 = %s" % return_tuple_value_level(tree1, result=[]))

    log.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 6 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    log.info("List of Tuple Value,Level for Tree2 = %s" % return_tuple_value_level(tree1, result=[]))

    log.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 7 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    log.info("List with elements of Tree1 sorted by level = %s" % sort_by_level(tree1))

    log.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 8 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    log.info("List with elements of Tree2 sorted by level = %s" % sort_by_level(tree2))

if __name__ == "__main__":
    global log
    # log_target expects: file | terminal
    log = utils.get_top_level_logger(name=__file__, log_target='terminal')
    try:
        main()
    # If it get any exception during execution, log it and exit.
    except Exception as e:
        msg = '%s failed to finish executing successfully.' % __file__
        log.exception(msg)
        #print(msg, '\n', str(e))
        sys.exit(1)

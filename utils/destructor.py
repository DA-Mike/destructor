import os
import shutil
import time

class Destructor:

    def __init__(self):
        self.__init__()

    def destroy(self, path):
        count = 0
        st = time.time()
        try:

            for dir, subdirs, files in os.walk(path):
                if os.path.isdir(dir) and dir == path + "\\node_modules":
                    # remove directory and all its content
                    shutil.rmtree(dir)
                    count += 1
                elif subdirs:
                    if len(subdirs) > 1:
                        for sub in subdirs:
                            if os.path.isdir(os.path.join(dir, sub)) and sub == "node_modules":
                                # remove directory and all its content
                                shutil.rmtree(os.path.join(dir, sub))
                                count += 1
                    else:
                        # verify path exists and it's node_modules
                        if os.path.isdir(os.path.join(dir, subdirs[0])) and subdirs[0] == "node_modules":
                            # remove directory and all its content
                            shutil.rmtree(os.path.join(dir, subdirs[0]))
                            count += 1
                elif len(files) > 0 or len(files) == 0:
                    pass
                else:
                    raise ValueError("Path {} is not a file or dir.".format(path))
            et = time.time()
            elapsed_time = et - st
            d_msg = "{} node_modules directories were destroyed!".format(count)
            time_msg = "Destroy() took {} seconds to execute".format(elapsed_time)
            return [d_msg, time_msg]

        except:
            return ['Error: ', 'An unknown error occurred.']

    def seek(self, path):
        count = 0
        st = time.time()
        try:

            for dir, subdirs, files in os.walk(path):
                if os.path.isdir(dir) and dir == path + "\\node_modules":
                    count += 1
                elif subdirs:
                    if len(subdirs) > 1:
                        for sub in subdirs:
                            if os.path.isdir(os.path.join(dir, sub)) and sub == "node_modules":
                                count += 1
                                subdirs.remove(sub)
                    else:
                        # verify path exists and it's node_modules
                        if os.path.isdir(os.path.join(dir, subdirs[0])) and subdirs[0] == "node_modules":
                            count += 1
                            subdirs.remove(subdirs[0])
                elif len(files) > 0 or len(files) == 0:
                    pass
                else:
                    raise ValueError("Path {} is not a file or dir.".format(path))
            et = time.time()
            elapsed_time = et - st
            s_msg = "There are {} node_modules directories set for destruction.".format(count)
            time_msg = "Seek() took {} seconds to execute".format(elapsed_time)
            return [s_msg, time_msg]
            
        except:
            return ['Error: ', 'An unknown error occurred.']
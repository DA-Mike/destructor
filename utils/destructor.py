import os
import shutil
import time


class Destructor:

    """This class has two main functions: Seek and Destroy all node_modules
    directories in the desired path"""

    # def __init__(self):
    #     """Init function"""
    #     self.__init__()

    def destroy(self, path):
        """This walks through the path and deletes node_modules directories.
        Returns array."""
        count = 0
        start_time = time.time()
        try:

            for dir, subdirs, files in os.walk(path):
                if os.path.isdir(dir) and dir == path + "\\node_modules":
                    # remove directory and all its content
                    shutil.rmtree(dir)
                    count += 1
                elif subdirs:
                    if len(subdirs) > 1:
                        for sub in subdirs:
                            if (
                                os.path.isdir(os.path.join(dir, sub))
                                and sub == "node_modules"
                            ):
                                # remove directory and all its content
                                shutil.rmtree(os.path.join(dir, sub))
                                count += 1
                    else:
                        # verify path exists and it's node_modules
                        if (
                            os.path.isdir(os.path.join(dir, subdirs[0]))
                            and subdirs[0] == "node_modules"
                        ):
                            # remove directory and all its content
                            shutil.rmtree(os.path.join(dir, subdirs[0]))
                            count += 1
                elif len(files) > 0 or len(files) == 0:
                    pass
                else:
                    raise ValueError(f"Path {path} is not a file or dir.")
            end_time = time.time()
            elapsed_time = end_time - start_time
            d_msg = f"{count} node_modules directories were destroyed!"
            time_msg = f"Destroy() took {elapsed_time} seconds to execute"
            return [d_msg, time_msg]

        except ValueError as err:
            return ["Error: ", err]
        except OSError as err:
            return ["Error: ", err]

    def seek(self, path):
        """Seeks out, counts, and returns the number of node_modules
        directories it finds in an array"""

        count = 0
        start_time = time.time()
        try:

            for dir, subdirs, files in os.walk(path):
                if os.path.isdir(dir) and dir == path + "\\node_modules":
                    count += 1
                elif subdirs:
                    if len(subdirs) > 1:
                        for sub in subdirs:
                            if (
                                os.path.isdir(os.path.join(dir, sub))
                                and sub == "node_modules"
                            ):
                                count += 1
                                subdirs.remove(sub)
                    else:
                        # verify path exists and it's node_modules
                        if (
                            os.path.isdir(os.path.join(dir, subdirs[0]))
                            and subdirs[0] == "node_modules"
                        ):
                            count += 1
                            subdirs.remove(subdirs[0])
                elif len(files) > 0 or len(files) == 0:
                    pass
                else:
                    raise ValueError(f"Path {path} is not a file or dir.")
            end_time = time.time()
            elapsed_time = end_time - start_time
            s_msg = f"There are {count} node_modules directories set for destruction."
            time_msg = f"Seek() took {elapsed_time} seconds to execute"
            return [s_msg, time_msg]

        except ValueError as err:
            return ["Error: ", err]
        except OSError as err:
            return ["Error: ", err]

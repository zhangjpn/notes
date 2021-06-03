
import io
import shutil

def string_io_to_file(filename):
    buf = io.StringIO()
    buf.write('11111')
    buf.seek(0)
    with open(filename, 'wt') as f:
        shutil.copyobj(buf, f)
    

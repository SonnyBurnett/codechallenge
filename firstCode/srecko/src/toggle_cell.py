from IPython.core.display import display, HTML

""" toggle_cell.py is a supporting python script for the notebooks.
    It helps on some of the limitations in vanilla notebooks installations to represent code cells.
"""
# TODO: see if the three warnings regarding tuples in the display method can be removed.

toggle_code_str = '''
<form action="javascript:code_toggle()"><input type="submit" id="toggleButton" value="Toggle Code"></form>
'''

toggle_code_prepare_str = '''
    <script>
    function code_toggle() {
        if ($('div.cell.code_cell.rendered.selected div.input').css('display')!='none'){
            $('div.cell.code_cell.rendered.selected div.input').hide();
        } else {
            $('div.cell.code_cell.rendered.selected div.input').show();
        }
    }
    </script>
'''

tag = HTML('''<script>
code_show=true; 
function code_toggle() {
    if (code_show){
        $('div.cell.code_cell.rendered.selected div.input').hide();
    } else {
        $('div.cell.code_cell.rendered.selected div.input').show();
    }
    code_show = !code_show
} 
$( document ).ready(code_toggle);
</script>
To show/hide this cell's raw code input, click <a href="javascript:code_toggle()">here</a>.''')

display(HTML(toggle_code_prepare_str + toggle_code_str))


def toggle_code():
    """ This adds a toggle code button under the output cell in a notebook.

    :return: none
    """
    display(HTML(toggle_code_str))


def toggle_link():
    """ This adds a toggle link button on top in the output cell of a notebook.

    :return: none
    """
    display(tag)

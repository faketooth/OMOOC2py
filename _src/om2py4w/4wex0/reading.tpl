%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<p>日记内容</p>
<a href='/'>Back to Home</a>
%for line in content:
    {{line}}<br />
%end

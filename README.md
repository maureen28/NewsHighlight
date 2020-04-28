# News Highlight

## Author : Maureen Wairimu

## Description
News Highlight is an application that helps users list and preview news articles from various sources.   
They are able to see various news sources on the application homepage, select a news source as well as see the image, description and the time a news article was created.

### Screenshot.
<img src="/Screenshot from 2020-04-28 09-36-51.jpg" alt="News Highlight" width="400"/>

## Setup Instructions
<ol>
<li>Clone or download the repository <code>https://github.com/maureen28/NewsHighlight.git</code> </li>
<li>Create a virtual environment
<pre>
<code>
pip install virtualenv
source virtual/bin/activate
</code></pre>
> To exit virtual environment you run the <code>deactivate</code> command
</li>
<li>Read the requirements.txt and install all the requirements using <code>pip install <name> </code></li>
<li>Create start.sh file in your directory</li>
<li>Go to the news API website and generate your API key then add it to start.sh</li>
<li> Run <code>chmod a+x start.sh </code></li>
<li>Run <code>./start.sh</code></li>
<li>Access the app through `localhost:5000`</li>
</ol>

### Live link :

## Technology & Dependency
<ol>
<li>python3.6</li>
<li>Pip</li>
<li>CSS(Bootstrap)</li>
<li>Flask Framework</li>
</ol>

## BDD
<table>
<tr>
<th>Behaviour</th>
<th>Input</th>
<th>Output</th>
</tr>
<tr>
<td>Display articles from a news source</td>
<td><strong>Click a news source</strong></td>
<td>Redirected to a page with a list of articles from the source</td>
</tr>
<tr>
<td>Display news sources</td>
<td><strong>On page load</strong></td>
<td>List of various news sources is displayed per category</td>
</tr>
<tr>
<td>Display the preview of an article</td>
<td><strong>On page load</strong></td>
<td>Each article displays an image, title, description and publication date</td>
</tr>
</table>

### Known Bugs
If you find a bug please feel free to alert me.
To fix the bug:
<ul list-style-type=circle;>
<li>Fork the repository</li>
<li>Open your terminal</li>
<li>Create a new branch</li>
<li>Make the changes, then (git add) to add changes</li>
<li>Commit the changes you have made(git commit -m"Fix bug") </li>
<li>Push changes made and click pull request so that I can access the changes made.</li>
</ul>

## Contact Information

To get in touch E-MAIL me on nimz69509@gmail.com

## License

MIT License
<b>Copyright (c) 2020 maureen28<b>

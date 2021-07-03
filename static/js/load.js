!function () {
    var name = 'sparsh';
    var div = document.createElement('div');
    div.setAttribute('class', 'row section-intro');
    div.innerHTML = `
    <div class="col-twelve">
    <h5>Portfolio</h5>
    <h1>Check Out Some of ${name}'s Works.</h1>

    <p class="lead">Lorem ipsum Do commodo in proident enim in dolor cupidatat adipisicing dolore officia nisi aliqua incididunt Ut veniam lorem ipsum Consectetur ut in in eu do.</p>
    </div>
    `;
    document.getElementById('portfolio').appendChild(div);
}
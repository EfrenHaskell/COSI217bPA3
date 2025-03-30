/*
Function creates comment form
to be called in note page
*/
function addComment() {
    let section = document.getElementById("AddComment");
    section.replaceChildren();
    let commentForm = document.createElement("form")
    let commentInput = document.createElement("input")
    let submit = document.createElement("input")
    // create form comment input and submit button elements
    commentForm.setAttribute("method", "post");
    commentForm.setAttribute("action", `/note${window.location.search}`);
    commentInput.setAttribute("name", "content")
    submit.setAttribute("type", "submit")
    commentForm.appendChild(commentInput)
    commentForm.appendChild(submit)
    section.appendChild(commentForm)
    // add to DOM
}


/*
Makes delete request, removing note and then redirects to home page
*/
function deleteNote() {
    fetch(`/note${window.location.search}`, {method: 'DELETE'})
        .then(function(response) {
            // redirect on successful delete
            if(response.ok) {
                window.location.href= "/";
            }
        });
}

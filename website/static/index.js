function deleteNote(noteId) {
    // send note.id to the delete-note endpoint
    fetch("/delete-note", {
        method: 'POST',
        body: JSON.stringify({ noteId: noteId}),
    }).then((_res) => {
        window.location.href = "/";
    });
}
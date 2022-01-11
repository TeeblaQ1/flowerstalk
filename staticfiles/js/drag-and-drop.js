let dropzone = document.querySelector('.drop-zone')
let dropzoneInput = document.querySelector ('.dropzone-input')

dropzone.addEventListener('click', e => {
    dropzoneInput.click()
})

dropzoneInput.addEventListener('change', e => {
    if (dropzoneInput.files.length) {
        console.log('Yeah', dropzoneInput.files)
        updateThumbnail(dropzone, dropzoneInput.files[0])
    }
})

dropzone.addEventListener('dragover', e => {
    e.preventDefault()
    dropzone.classList.add('over')
})

let dragEvents = ["dragleave", "dragend"]
dragEvents.forEach(type => {
    dropzone.addEventListener(type, e => {
        e.preventDefault()
        dropzone.classList.remove('over')
    })
})
dropzone.addEventListener('drop', e => {
    e.preventDefault()
     if (e.dataTransfer.files.length) {
         dropzoneInput.files = e.dataTransfer.files
         updateThumbnail(dropzone, e.dataTransfer.files[0])
     }
     dropzone.classList.remove('over')
})

function updateThumbnail(dropzone, file) {
    let thumbnailElement = dropzone.querySelector('.drop-zone-img')

    if (dropzone.querySelector('.drop-zone-text')) {
        dropzone.querySelector('.drop-zone-text').remove()
    }

    if(!thumbnailElement) {
        thumbnailElement = document.createElement('div')
        thumbnailElement.classList.add('drop-zone-img')
        dropzone.appendChild(thumbnailElement)
    }

    if (file.type.startsWith('image/')) {
        const reader = new FileReader()

        reader.readAsDataURL(file)
        reader.onload = () => {
            thumbnailElement.style.backgroundImage = `url('${reader.result}')`
        }
    } else {
        thumbnailElement.style.backgroundImage = null
    }
}

function fillUploadForm(){
    let proofDetailsInputs = document.querySelector('.proof-details')
    let formValues = {}
    for (let i = 0; i < proofDetailsInputs.children.length; i++){
        if((proofDetailsInputs.children[i].tagName != 'P') && (proofDetailsInputs.children[i].tagName != 'BUTTON')){
            if(proofDetailsInputs.children[i].getAttribute('name') == 'orderItem'){
                formValues[proofDetailsInputs.children[i].getAttribute('name')] = parseInt(proofDetailsInputs.children[i].value.slice(6)).toString()
            } else {
                formValues[proofDetailsInputs.children[i].getAttribute('name')] = proofDetailsInputs.children[i].value
            }
        }
    }
    for (const [key, value] of Object.entries(formValues)){
        document.querySelector('form.payment-upload-form').elements[key].value = value
    }

    console.log(formValues)
    document.querySelector('form.payment-upload-form').submit()
}


// MODAL

// Get the modal element
let modalDiv = document.getElementById("modal-div");
let avatarImage = document.getElementById("avatar-img");

// Get the image and text elements inside the modal
let modalImage = document.getElementById("modal-image");
let modalText = document.getElementById("modal-text");
let modalTitle = document.querySelector("#modal-box h2");
let modalContent = document.getElementById("modal-display-content")

// Function to open the modal and display the content with fade-in effect
function openModal(imageSrc, textContent, titleContent) {
  modalDiv.style.display = "block";
  modalContent.classList.add("fade-in");
  closeButton.style.display = "block";
  modalImage.src = imageSrc;
  modalImage.classList.remove("fade-in"); 
  void modalImage.offsetWidth; 
  modalImage.classList.add("fade-in");
  modalText.innerText = textContent;
  modalText.classList.remove("fade-in");
  void modalText.offsetWidth;
  modalText.classList.add("fade-in");
  modalTitle.innerText = titleContent;
  modalTitle.classList.remove("fade-in");
  void modalTitle.offsetWidth;
  modalTitle.classList.add("fade-in");
  modalImage.style.display = "block";
  modalTitle.style.display = "block";
  avatarImage.style.opacity = "1";
  document.getElementById("static-modal-content").style.display = "none";
}

// Function to close the modal
function closeModal() {
  modalDiv.style.display = "none";
  showStaticModal();
}

// Close the modal when clicking outside of it
document.addEventListener("click", function (event) {
  const targetElement = event.target;
  if (
    !modalDiv.contains(targetElement) &&
    !targetElement.classList.contains("modal-image")
  ) {
    closeModal();
  }
});

let closeButton = document.querySelector(".modal-close-button");
closeButton.addEventListener("click", function () {
  closeModal();
});

let icons = document.querySelectorAll(".modal-image");
icons.forEach(function (icon) {
  icon.addEventListener("click", function () {
    let imageSrc = icon.src;
    let textContent = icon.title;
    let titleContent = icon.alt;
    openModal(imageSrc, textContent, titleContent);
  });
});

function showStaticModal() {
  modalText.innerText = "Click on the icons for more info!";
  modalText.style.textAlign = "center";
  modalImage.style.display = "none";
  modalTitle.style.display = "none";
  closeButton.style.display = "none";
  document.getElementById("static-modal-content").style.display = "block";
}


// Call the showStaticModal function on page load
showStaticModal();



// animated text in 'Projects' Section

const projectImages = document.querySelectorAll(".card");
const loremParagraph = document.querySelector(".lorem-text");

let typingTimer;

function typeLoremText(text) {
  let index = 0;
  loremParagraph.textContent = "";
  clearInterval(typingTimer);
  typingTimer = setInterval(() => {
    if (index < text.length) {
      loremParagraph.textContent += text.charAt(index);
      index++;
    } else {
      clearInterval(typingTimer);
    }
  }, 15);
}

function resetLoremText(text) {
  clearInterval(typingTimer);
  typeLoremText(text);
}

projectImages.forEach((image) => {
  const projectExtraInfo = image.parentElement.querySelector(".lorem-text").dataset.extraInfo;

  image.addEventListener("mouseenter", () => {
    resetLoremText(projectExtraInfo);
  });

  image.addEventListener("mouseleave", () => {
    resetLoremText(projectExtraInfo);
  });
});

loremParagraph.style.display = "none";

document.addEventListener("DOMContentLoaded", () => {
  projectImages.forEach((image) => {
    const projectExtraInfo = image.parentElement.querySelector(".lorem-text").dataset.extraInfo;

    image.addEventListener("mouseenter", () => {
      loremParagraph.style.display = "block";
      resetLoremText(projectExtraInfo);
    });

    image.addEventListener("mouseleave", () => {
      loremParagraph.style.display = "none";
      resetLoremText(projectExtraInfo);
    });
  });
});


// Animation for 'intro-paragraphs' in 'headings' section

let renderText = (paragraph, text) => {
  return new Promise((resolve) => {
    let currentIndex = 0;
    paragraph.textContent = "";

    let renderNextCharacter = () => {
      if (currentIndex < text.length) {
        if (text[currentIndex] === "!" || text[currentIndex] === ".") {
          // Add a longer pause after periods and exclamation marks
          paragraph.textContent += text.charAt(currentIndex);
          currentIndex++;
          setTimeout(() => {
            renderNextCharacter();
          }, 1000);
        } else {
          paragraph.textContent += text.charAt(currentIndex);
          currentIndex++;
          setTimeout(renderNextCharacter, 10);
        }
      } else {
        resolve();
      }
    };

    renderNextCharacter();
  });
};


let animateParagraphsSequentially = async (paragraphs) => {
  for (let i = 0; i < paragraphs.length; i++) {
    const paragraph = paragraphs[i];
    const text = paragraph.textContent;
    await renderText(paragraph, text);

    // Add a longer pause after the second intro-paragraph
    if (i === 1) {
      await new Promise((resolve) => {
        setTimeout(resolve, 2000);
      });
    }
  }
};

let introPar1 = document.querySelector(".intro-par-1");
let introPar2 = document.querySelector(".intro-par-2");
let statusImages = document.querySelectorAll(".status-images , .status-text, .study-images");

// Hide intro-par-2 and status-images initially
introPar2.style.opacity = "0";
statusImages.forEach((image) => {
  image.style.opacity = "0";
});

// Start animating intro-par-1
animateParagraphsSequentially([introPar1]).then(() => {
  // Delay before animating intro-par-2
  setTimeout(() => {
    introPar2.style.opacity = "1";
    animateParagraphsSequentially([introPar2]).then(() => {
      // Delay before fading in status-images
      setTimeout(() => {
        statusImages.forEach((image, index) => {
          setTimeout(() => {
            image.style.opacity = "1";
          }, (index + 1) * 1000);
        });
      }, 50);
    });
  }, 150);
});

// Set up scene, camera, and renderer
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Add a cube
const geometry = new THREE.BoxGeometry();
const material = new THREE.MeshBasicMaterial({ color: 0x00ff00, wireframe: true });
const cube = new THREE.Mesh(geometry, material);
scene.add(cube);
camera.position.z = 5;

let isMovingForward = false;
let isMovingBackward = false;
let isMovingLeft = false;
let isMovingRight = false;
let isRotating = false;
let mouseDown = false;

const moveSpeed = 0.1;
const rotateSpeed = 0.01;

document.addEventListener('keydown', (event) => {
    switch (event.key) {
        case 'w':
            isMovingForward = true;
            break;
        case 's':
            isMovingBackward = true;
            break;
        case 'a':
            isMovingLeft = true;
            break;
        case 'd':
            isMovingRight = true;
            break;
    }
});

document.addEventListener('keyup', (event) => {
    switch (event.key) {
        case 'w':
            isMovingForward = false;
            break;
        case 's':
            isMovingBackward = false;
            break;
        case 'a':
            isMovingLeft = false;
            break;
        case 'd':
            isMovingRight = false;
            break;
    }
});

// To capture canvas click and toggle rotation mode
renderer.domElement.addEventListener('click', () => {
    isRotating = !isRotating;
});

document.addEventListener('mousemove', (event) => {
    if (isRotating) {
        camera.rotation.y -= event.movementX * rotateSpeed;
        camera.rotation.x -= event.movementY * rotateSpeed;
    }
});

function animate() {
    requestAnimationFrame(animate);

    if (isMovingForward) camera.position.z -= moveSpeed;
    if (isMovingBackward) camera.position.z += moveSpeed;
    if (isMovingLeft) camera.position.x -= moveSpeed;
    if (isMovingRight) camera.position.x += moveSpeed;

    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;

    renderer.render(scene, camera);
}

window.addEventListener('resize', () => {
    renderer.setSize(window.innerWidth, window.innerHeight);
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
});

animate();

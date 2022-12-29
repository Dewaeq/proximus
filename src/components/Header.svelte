<nav>
    <div>
        <h1>Product title</h1>
    </div>
    <div id="nav-links">
        <div class="nav-item">
            <p>first item</p>
        </div>
        <div class="nav-item">
            <p>second item</p>
        </div>
        <div class="nav-item">
            <p>third item</p>
        </div>
    </div>
</nav>

<style>
    nav {
        display: flex;
        justify-content: space-between;
        justify-items: center;
        padding: 0 40px;
        color: white;
        background-color: #2e2d2d;
    }

    #nav-links {
        display: flex;
        align-items: center;
        font-weight: bold;
    }
    .nav-item {
        padding: 0 15px;
    }
</style>

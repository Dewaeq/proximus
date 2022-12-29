<script lang="ts">
    export let text: String;
</script>

<div class="wrapper">
    <p>{text}</p>
</div>

<style>
    .wrapper {
        border: 2px solid rgb(245, 192, 19);
        border-radius: 8px;
        width: 40%;
        max-width: 500px;
        padding: 0 15px;
        margin: 40px 0;
        text-align: center;
    }

    @media only screen and (max-width: 600px) {
        .wrapper {
            width: 90%;
        }
    }

</style>
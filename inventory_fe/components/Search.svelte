<script lang="ts">
    export let searchKeyword;

    $: if ($searchKeyword) {
        const searchParams = new URLSearchParams(window.location.search);

        searchParams.set("name", $searchKeyword);

        const newUrl =
            window.location.protocol +
            "//" +
            window.location.host +
            window.location.pathname +
            "?" +
            searchParams.toString();

        window.history.pushState({ path: newUrl }, "", newUrl);
    }
</script>

<input type="text" class="form-control" bind:value={$searchKeyword} />

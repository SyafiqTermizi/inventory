<table class="table table-hover">
    <thead>
        <tr>
            <th scope="col">Name</th>
            <th scope="col">Supplier</th>
            <th scope="col">Availability</th>
        </tr>
    </thead>
    <tbody>
        {#each Array(2) as _}
            <tr>
                <td>
                    <p class="card-text placeholder-glow">
                        <span class="placeholder col-4"></span>
                    </p>
                </td>
                <td>
                    <p class="card-text placeholder-glow">
                        <span class="placeholder col-6"></span>
                    </p>
                </td>
                <td>
                    <p class="card-text placeholder-glow">
                        <span class="placeholder col-4"></span>
                    </p>
                </td>
            </tr>
        {/each}
    </tbody>
</table>

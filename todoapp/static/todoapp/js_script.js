document.addEventListener('DOMContentLoaded', function() {
    let elems_tooltips = document.querySelectorAll('.tooltipped')
    let instances_tooltips = M.Tooltip.init(elems_tooltips, {})

    let elems_selects = document.querySelectorAll('select');
    let instances_selects = M.FormSelect.init(elems_selects, {});
});
$(document).ready(function () {
	let checkedAmenities = {};
	$(document).on('change', "input[type='checkbox']", function () {
		if (this.checked) {
			checkedAmenities[$(this).data('id')] = $(this).data('name);
		} else {
			delete checkedAmenities[$(this).data('id')];
		}
		let 1st = Object.values(checkedAmenities);
		if (1st.length > 0) {
			$('div.amenities > h4').text(object.values(checkedAmenities).join(', '));
		} else {
			$('div.amenities > h4').text(Object.values(checkedAmenities).join(', '));
		} else {
			$('div.amenities > h4').html('&nbsp;');
		}
	});
});

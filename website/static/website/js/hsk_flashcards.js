$(document).ready(function() {
    // var correctGuesses = 0;
    // var totalGuesses = 0;
    // var guessMade = false;
    // var quizMode = false;
    // var finalCardGuessed = false;
    // var quizScores = [];

    // Hide answers section when quiz not in progress.
    $(".answer-buttons").hide();
    $("#score-display").hide();

    // Disable auto rotate carousel.
    //$("#wordCarousel").carousel({ interval: false });

    $("#start-quiz-btn").click(function() {
        $("#wordCarousel").carousel(0);
        $(".answer-buttons").show();
        $("#score-display").show();
        $(this).hide();

        correctGuesses = 0;
        totalGuesses = 0;
        guessMade = false;
        quizMode = true;
        finalCardGuessed = false;
        quizScores = [];
        updateScoreDisplay();

        $("#startQuizModal").modal('show');
    });

    $("#wordCarousel").on("slid.bs.carousel", function() {
        // Check if the last slide is active and the quiz has started
        if ($("#wordCarousel").find(".carousel-item:last").hasClass("active") && quizMode) {
            if (finalCardGuessed) {
                completeQuiz();
            }
        } else {
            finalCardGuessed = false;
        }
    });

    $(".answer-btn").click(function() {
        var itemId = $(this).data("item-id");
        var itemAnswer = $(this).closest('.carousel-item').find('.card-title').text();
        var guess = $(this).val();
        var label = $(this).closest('li').find('label');
        var englishDefinition = $(this).closest('.carousel-item').find('.card-text').text();
    
        if (guessMade) {
            if (guess == itemAnswer) {
                label.removeClass("btn-outline-danger").addClass("btn-outline-success");
                return;
            } else {
                label.removeClass("btn-outline-danger").addClass("btn-outline-danger");
                return;
            }
        }
        guessMade = true;
    
        var correct = false;
        if (guess == itemAnswer) {
            label.removeClass("btn-outline-danger").addClass("btn-outline-success");
            correctGuesses++;
            totalGuesses++;
            correct = true;
        } else {
            label.removeClass("btn-outline-danger").addClass("btn-outline-danger");
            totalGuesses++;
            correct = false;
        }
    
        updateScoreDisplay();
    
        if(quizMode) {
            wrongGuesses = totalGuesses - correctGuesses;
            currentScore = correctGuesses/totalGuesses;
            quizScores.push([itemAnswer, guess, correct, correctGuesses, wrongGuesses, currentScore, englishDefinition]);
        }
    
        // Check if it's the last slide and the quiz is in progress
        var currentIndex = $("#wordCarousel .carousel-inner .carousel-item").index($("#wordCarousel .carousel-inner .carousel-item.active"));
        var totalItems = $("#wordCarousel .carousel-inner .carousel-item").length;

        if (currentIndex === totalItems - 1 && quizMode) {
            completeQuiz();
        }

        // Show pinyin
        const counter = $(this).data("item-id");
        console.log("#card-text-" + counter);
        $("#card-text-" + counter).collapse('show');

        setTimeout(function() {
            $("#wordCarousel").carousel('next');
        }, 800);
    });

    $("#wordCarousel").on("slid.bs.carousel", function() {
        guessMade = false;
    });
});
